﻿/*
 * (c) Copyright Ascensio System SIA 2010-2021
 *
 * This program is a free software product. You can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License (AGPL)
 * version 3 as published by the Free Software Foundation. In accordance with
 * Section 7(a) of the GNU AGPL its Section 15 shall be amended to the effect
 * that Ascensio System SIA expressly excludes the warranty of non-infringement
 * of any third-party rights.
 *
 * This program is distributed WITHOUT ANY WARRANTY; without even the implied
 * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For
 * details, see the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
 *
 * You can contact Ascensio System SIA at 20A-12 Ernesta Birznieka-Upisha
 * street, Riga, Latvia, EU, LV-1050.
 *
 * The  interactive user interfaces in modified source and object code versions
 * of the Program must display Appropriate Legal Notices, as required under
 * Section 5 of the GNU AGPL version 3.
 *
 * Pursuant to Section 7(b) of the License you must retain the original Product
 * logo when distributing the program. Pursuant to Section 7(e) we decline to
 * grant you any rights under trademark law for use of our trademarks.
 *
 * All the Product's GUI elements, including illustrations and icon sets, as
 * well as technical writing content are licensed under the terms of the
 * Creative Commons Attribution-ShareAlike 4.0 International. See the License
 * terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode
 *
 */
#pragma once

#include "./FileTransporter_private.h"
#include "../include/FileTransporter.h"

namespace NSNetwork
{
    namespace NSFileTransport
    {
        CFileTransporter::CFileTransporter(const std::wstring &sDownloadFileUrl, bool bDelete)
        {
            m_pInternal = new CFileTransporter_private(sDownloadFileUrl, bDelete);
        }

        CFileTransporter::CFileTransporter(const std::wstring &sUploadUrl, const unsigned char* cData, const int nSize)
        {
            m_pInternal = new CFileTransporter_private(sUploadUrl, cData, nSize);
        }

        CFileTransporter::CFileTransporter(const std::wstring &sUploadUrl, const std::wstring &sUploadFilePath)
        {
            m_pInternal = new CFileTransporter_private(sUploadUrl, sUploadFilePath);
        }

        CFileTransporter::~CFileTransporter()
        {
            Stop();
            if (NULL != m_pInternal)
                delete m_pInternal;
        }

        void CFileTransporter::SetDownloadFilePath(const std::wstring& sDownloadFilePath)
        {
            return m_pInternal->SetDownloadFilePath(sDownloadFilePath);
        }

        std::wstring CFileTransporter::GetDownloadFilePath()
        {
            return m_pInternal->GetDownloadFilePath();
        }

        bool CFileTransporter::IsFileDownloaded()
        {
            return m_pInternal->IsFileDownloaded();
        }

        void CFileTransporter::SetDownloadFileUrl(const std::wstring &sDownloadFileUrl, bool bDelete)
        {
            m_pInternal->SetDownloadFileUrl(sDownloadFileUrl, bDelete);
        }

        bool CFileTransporter::DownloadSync()
        {
            return m_pInternal->TransferSync();
        }

        void CFileTransporter::DownloadAsync()
        {
            m_pInternal->TransferAsync();
        }

        void CFileTransporter::SetUploadUrl(const std::wstring &sUploadUrl)
        {
            m_pInternal->SetUploadUrl(sUploadUrl);
        }

        void CFileTransporter::SetUploadBinaryData(const unsigned char* cData, const int nSize)
        {
            m_pInternal->SetUploadBinaryDara(cData, nSize);
        }

        void CFileTransporter::SetUploadFilePath(const std::wstring &sUploadFilePath)
        {
            m_pInternal->SetUploadFilePath(sUploadFilePath);
        }

        bool CFileTransporter::UploadSync()
        {
            return m_pInternal->TransferSync();
        }

        void CFileTransporter::UploadAsync()
        {
            m_pInternal->TransferAsync();
        }

        std::wstring& CFileTransporter::GetResponse()
        {
            return m_pInternal->GetResponse();
        }

        void CFileTransporter::Start(int lPriority)
        {
            return m_pInternal->Start(lPriority);
        }

        void CFileTransporter::Suspend()
        {
            return m_pInternal->Suspend();
        }

        void CFileTransporter::Resume()
        {
            return m_pInternal->Resume();
        }

        void CFileTransporter::Stop()
        {
            return m_pInternal->Stop();
        }

        int CFileTransporter::IsSuspended()
        {
            return m_pInternal->IsSuspended();
        }

        int CFileTransporter::IsRunned()
        {
            return m_pInternal->IsRunned();
        }

        int CFileTransporter::GetError()
        {
            return m_pInternal->GetError();
        }

        int CFileTransporter::GetPriority()
        {
            return m_pInternal->GetPriority();
        }

        void CFileTransporter::CheckSuspend()
        {
            return m_pInternal->CheckSuspend();
        }

        void CFileTransporter::SetEvent_OnProgress(CFileTransporter_OnProgress func)
        {
            m_pInternal->GetInternal()->m_func_onProgress = func;
        }

        void CFileTransporter::SetEvent_OnComplete(CFileTransporter_OnComplete func)
        {
            m_pInternal->GetInternal()->m_func_onComplete = func;
        }

        #ifdef _MAC
        bool CFileTransporter::m_bIsARCEnabled = false;

        void CFileTransporter::SetARCEnabled(const bool& enabled)
        {
            m_bIsARCEnabled = enabled;
        }

        bool CFileTransporter::GetARCEnabled()
        {
            return m_bIsARCEnabled;
        }
        #endif
    }
}